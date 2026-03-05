const express = require('express');
const app = express();

app.use(express.json());

let books = [
  { id: 1, title: 'Harry Potter and the Philosopher\'s Stone', author: 'J.K. Rowling', status: 'available' },
  { id: 2, title: 'Nobita\'s Secret Gadget Museum', author: 'Fujiko F. Fujio', status: 'borrowed' },
];

app.get('/api/books', async (req, res) => {
    try {
        res.json(books)
    } catch (error) {
        console.error('Error fetching books:', error);
        res.status(500).json({ error: 'An error occurred while fetching books' });
    }
});

app.post('/api/books', async (req, res) => {
    try {
        const { title, author, status } = req.body;
        const newBook = { id: books.length + 1, title, author, status };
        books.push(newBook);
        res.status(201).json(newBook);
    } catch (error) {
        console.error('Error adding book:', error);
        res.status(500).json({ error: 'Server error' });
    }
});

app.delete('/api/books/:id', async (req, res) => {
    try {
        const bookId = parseInt(req.params.id);
        books = books.filter(book => book.id !== bookId);
        res.status(200).json({ message: 'Book deleted successfully' });
    } catch (error) {
        console.error('Error deleting book:', error);
        res.status(500).json({ error: 'Server error' });
    }
});

app.put('/api/books/:id', async (req, res) => {
    try {
        const bookId = parseInt(req.params.id);
        const { title, author, status } = req.body;
        const bookIndex = books.findIndex(book => book.id === bookId);
        if (bookIndex == -1) {
            return res.status(404).json({ error: 'Book not found' });
        }
        books[bookIndex] = { ...books[bookIndex], title, author, status };
        res.json(books[bookIndex]);
    } catch (error) {
        console.error('Error updating book:', error);
        res.status(500).json({ error: 'Server error' });
    }
});

app.patch('/api/books/:id', async (req, res) => {
    try {
        const bookId = parseInt(req.params.id);     
        const bookIndex = books.findIndex(book => book.id === bookId);  
        if (bookIndex == -1) {
            return res.status(404).json({ error: 'Book not found' });
        }
        const status = req.body.status;
        if (status) {
            books[bookIndex].status = status;
        }
        res.json(books[bookIndex]);
    } catch (error) {
        console.error('Error updating book:', error);
        res.status(500).json({ error: 'Server error' });
    }
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});