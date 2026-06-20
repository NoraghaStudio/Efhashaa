const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '')));

// Database setup
const db = new sqlite3.Database('./database.sqlite', (err) => {
    if (err) {
        console.error('Error opening database', err);
    } else {
        console.log('Connected to the SQLite database.');
        db.run(`CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT,
            text TEXT,
            isHaraj BOOLEAN DEFAULT 1,
            phone TEXT,
            rating TEXT DEFAULT 'positive',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )`);
    }
});

// API Routes
// Get reviews
app.get('/api/reviews', (req, res) => {
    db.all('SELECT * FROM reviews ORDER BY id DESC', [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

// Add a new review
app.post('/api/reviews', (req, res) => {
    const { name, date, text, isHaraj, phone, rating } = req.body;
    db.run(
        `INSERT INTO reviews (name, date, text, isHaraj, phone, rating) VALUES (?, ?, ?, ?, ?, ?)`,
        [name, date, text, isHaraj === false ? 0 : 1, phone, rating || 'positive'],
        function(err) {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ id: this.lastID });
        }
    );
});

// Update review status
app.put('/api/reviews/:id', (req, res) => {
    const { name, text, isHaraj } = req.body;
    db.run(
        `UPDATE reviews SET name = ?, text = ?, isHaraj = ? WHERE id = ?`,
        [name, text, isHaraj === false ? 0 : 1, req.params.id],
        function(err) {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ updated: this.changes });
        }
    );
});

// Delete a review
app.delete('/api/reviews/:id', (req, res) => {
    db.run(
        `DELETE FROM reviews WHERE id = ?`,
        req.params.id,
        function(err) {
            if (err) return res.status(500).json({ error: err.message });
            res.json({ deleted: this.changes });
        }
    );
});

// Simple Login endpoint for Admin
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    // Hardcoded simple auth for self-hosting without Supabase
    if (email === 'admin' && password === 'admin123') { // Replace with strong password
        res.json({ token: 'valid-admin-session' });
    } else {
        res.status(401).json({ error: 'Invalid credentials' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Access the admin panel at http://localhost:${PORT}/admin.html`);
});
