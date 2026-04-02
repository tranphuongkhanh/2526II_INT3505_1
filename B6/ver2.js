// ver2.js: thêm phân quyền
// Ở đây có 2 role là admin và reader, chỉ admin mới được thểm, sửa, xóa sách. Reader chỉ được xem sách.
const express = require('express');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');
const crypto = require('crypto');
const app = express();
app.use(express.json());
app.use(cookieParser());

const SECRET_KEY = 'secret_key_ver1';
const REFRESH_SECRET_KEY = 'secret_refresh_key';
const users = [
    { id: 1, username: 'admin', password: '123', role: 'admin' }, 
    { id: 2, username: 'reader', password: '123', role: 'reader' }
];
let books = [
    { id: 1, title: 'Clean Code', author: 'Robert C. Martin', status: 'available' },
    { id: 2, title: 'The Pragmatic Programmer', author: 'Andrew Hunt', status: 'borrowed' }
];
let refreshTokens = [];
let revokedJtis = [];

app.post('/api/login', (req, res) => {
    const user = users.find(u => u.username === req.body.username && u.password === req.body.password);
    if (!user) return res.status(401).json({ message: 'Sai thông tin' });

    const uniqueTokenId = crypto.randomUUID();

    const accessToken = jwt.sign(
        { id: user.id, username: user.username, role: user.role, jti: uniqueTokenId }, 
        SECRET_KEY, 
        { expiresIn: '1m', algorithm: 'HS256' }
    );

    const refreshToken = jwt.sign(
        { id: user.id, username: user.username, role: user.role, jti: crypto.randomUUID() }, 
        REFRESH_SECRET_KEY, 
        { expiresIn: '7d', algorithm: 'HS256' }
    );
    refreshTokens.push(refreshToken);

    res.cookie('refreshToken', refreshToken, {
        httpOnly: true,// Chống XSS (JavaScript không đọc được)
        secure: false,// Set = true nếu chạy trên HTTPS
        sameSite: 'strict', // Chống tấn công CSRF
        maxAge: 7 * 24 * 60 * 60 * 1000 // Hạn sử dụng: 7 ngày (tính bằng milliseconds)
    });

    res.json({ accessToken });
});

app.post('/api/refresh-token', (req, res) => {
    const token = req.cookies.refreshToken;

    if (!token) return res.status(401).json({ message: 'Thiếu Refresh Token trong Cookie' });
    if (!refreshTokens.includes(token)) return res.status(403).json({ message: 'Refresh Token không tồn tại trong hệ thống' });

    jwt.verify(token, REFRESH_SECRET_KEY, (err, user) => {
        if (err) return res.status(403).json({ message: 'Refresh Token đã hết hạn' });

        const newPayload = { id: user.id, username: user.username, role: user.role, jti: crypto.randomUUID() };
        
        const newAccessToken = jwt.sign(newPayload, SECRET_KEY, { expiresIn: '1m' });
        
        res.json({ accessToken: newAccessToken });
    });
});

app.post('/api/logout', verifyToken, (req, res) => {
    const token = req.cookies.refreshToken;
    refreshTokens = refreshTokens.filter(t => t !== token);
    res.clearCookie('refreshToken');

    const tokenJti = req.user.jti;
    revokedJtis.push(tokenJti);
    
    res.json({ message: 'Đăng xuất thành công, Refresh Token đã bị vô hiệu hóa!' });
});

const verifyToken = (req, res, next) => {
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.status(401).json({ message: 'Thiếu Token' });
    try {
        const decoded = jwt.verify(
            token, 
            SECRET_KEY, 
            {algorithms: ['HS256']}
        );

        if (revokedJtis.includes(decoded.jti)) {
            return res.status(401).json({ message: 'Token này đã bị thu hồi (Bạn đã đăng xuất trước đó)' });
        }
    
        req.user = decoded;
        next();
    } catch (err) {
        return res.status(403).json({message: 'Token không hợp lệ hoặc đã hết hạn.'});
    }
};

app.use('/api/books', verifyToken);

function authorizeRole(role) {
  return (req, res, next) => {
    if (req.user.role !== role) {
      return res.status(403).json({ message: "Không có quyền thực hiện!" });
    }
    next();
  };
}

app.get('/api/books', (req, res) => {
    res.json(books);
});

app.get('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).json({ message: 'Không tìm thấy sách' });
    res.json(book);
});

app.post('/api/books', authorizeRole('admin'), (req, res) => {
    const { title, author, status } = req.body;
    const newBook = { 
        id: books.length > 0 ? books[books.length - 1].id + 1 : 1, 
        title, 
        author, 
        status
    };
    books.push(newBook);
    res.status(201).json(newBook);
});

app.put('/api/books/:id', authorizeRole('admin'), (req, res) => {
    const { title, author, status } = req.body;
    const bookIndex = books.findIndex(b => b.id === parseInt(req.params.id));
    
    if (bookIndex === -1) return res.status(404).json({ message: 'Không tìm thấy sách' });

    const oldBook = books[bookIndex];

    books[bookIndex] = {
        id: oldBook.id,
        title: title || oldBook.title,
        author: author || oldBook.author,
        status: status || oldBook.status
    };

    res.json(books[bookIndex]);
});

app.delete('/api/books/:id', authorizeRole('admin'), (req, res) => {
    const bookIndex = books.findIndex(b => b.id === parseInt(req.params.id));
    if (bookIndex === -1) return res.status(404).json({ message: 'Không tìm thấy sách' });

    books.splice(bookIndex, 1);
    res.json({ message: 'Đã xóa sách thành công' });
});

app.listen(3000, () => console.log('Ver 2 is running on http://localhost:3000/api/books'));