// ver0.js
const express = require('express');
const app = express();
app.use(express.json());

let books = [
    { id: 1, title: 'Clean Code', author: 'Robert C. Martin', status: 'available' },
    { id: 2, title: 'The Pragmatic Programmer', author: 'Andrew Hunt', status: 'borrowed' }
];

app.get('/api/books', (req, res) => {
    res.json(books);
});

app.get('/api/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).json({ message: 'Không tìm thấy sách' });
    res.json(book);
});

app.post('/api/books', (req, res) => {
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

app.put('/api/books/:id', (req, res) => {
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

app.delete('/api/books/:id', (req, res) => {
    const bookIndex = books.findIndex(b => b.id === parseInt(req.params.id));
    if (bookIndex === -1) return res.status(404).json({ message: 'Không tìm thấy sách' });

    books.splice(bookIndex, 1);
    res.json({ message: 'Đã xóa sách thành công' });
});

app.listen(3000, () => console.log('Ver 0 is running on http://localhost:3000/api/books'));