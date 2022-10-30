const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express()
const cors = require("cors");

app.use(cors());
app.use(express.json());
app.put('/uberdata', (req, res) => {
    const name = req.body.name;
    const password = req.body.password;
    const db = new sqlite3.Database('./uberdb.db', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error(err.message);
        }
        else {
            console.log('Connected to the database.');
        }
    });
    db.serialize(() => {
        //db.each(`SELECT stocktickers,chromosome,max(sharpe) FROM garesults WHERE date='${day}'`, (err, row) => {
        db.each(`SELECT name,destination FROM userprofile WHERE name is ? AND password is ?`, 
        [name, password],
        (err, row) => {
            if (err) {
                console.error(err.message);
            }
            console.log(row)
            res.send(row)
        });
    });
});
app.post('/register', (req, res) => {
    const name = req.body.name;
    const password = req.body.password;
    const destination = req.body.destination;
    const db = new sqlite3.Database('./uberdb.db', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error(err.message);
        }
        else {
            console.log('Connected to the database.');
        }
    });
    db.serialize(() => {
        //db.each(`SELECT stocktickers,chromosome,max(sharpe) FROM garesults WHERE date='${day}'`, (err, row) => {
        db.each(`INSERT INTO userprofile (name, password, destination) VALUES (?,?,?)`, 
        [name, password,destination],
        (err, row) => {
            if (err) {
                console.error(err.message);
            }
            res.send("Values Inserted");
        });
    });
});
app.listen(3001, () => {
    console.log('listening on port 3001')
})