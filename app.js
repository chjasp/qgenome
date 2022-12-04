const express = require("express");
const mysql = require("mysql");

// Create MySQL-Connection
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'bestday13',
    database: 'reddit_health'
});

// Connect
db.connect((err) => {
    if(err) {
        throw err;
    } 
    console.log("MySQL ...")
})

const app = express();

app.get('/', (req, res) => {
    console.log("YEAH")
})

app.get('/getposition/:pos', (req, res) => {
    let sql = `SELECT genotype FROM reddit_health.genome WHERE position = ${req.params.pos}`;
    db.query(sql, (err, result) => {
        if(err) throw err;
        console.log(result)
        let json_geno = Object.values(JSON.parse(JSON.stringify(result)))
        res.send(`Genotype: ${json_geno[0].genotype}`)
    })
})

app.listen('3000', () => {
    console.log('Server started on port 3000');
});