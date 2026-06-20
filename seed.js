const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

const db = new sqlite3.Database('./database.sqlite');
const reviews = JSON.parse(fs.readFileSync('extracted_reviews.json', 'utf-8'));

db.serialize(() => {
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

    db.run(`DELETE FROM reviews`); // Clear previous if any

    const stmt = db.prepare(`INSERT INTO reviews (name, date, text, isHaraj, rating) VALUES (?, ?, ?, ?, ?)`);
    reviews.forEach(r => {
        stmt.run(r.name, r.date, r.text, 1, 'positive');
    });
    stmt.finalize();

    console.log("Seeded " + reviews.length + " reviews.");
});

db.close();
