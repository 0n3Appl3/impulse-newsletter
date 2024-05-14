const dotenv = require('dotenv').config({
    path: '.env',
})
const https = require('https')
const fs = require('fs')
const bodyParser = require('body-parser')
const cors = require('cors')
const express = require('express')
const { connectDb } = require('./database/sequelize')
const emailRoutes = require('./routes/emailRoutes')
const newsletterRoutes = require('./routes/newsletterRoutes')
const app = express()
const port = process.env.PORT
const localPort = process.env.LOCAL_PORT

/*
 * REST API endpoint naming properties.
 */
const appContext = 'api'
const appVersion = 'v1'
const prefix =  '/' + appContext + '/' + appVersion

/* 
 * Enable Cross-Origin Resource Sharing.
 */
app.use(cors())

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false,
}))

/*
 * Establish REST API routes.
 */
app.use(prefix + '/email', emailRoutes)
app.use(prefix + '/newsletter', newsletterRoutes)

// Endpoint not found.
app.all('*', (req, res) => {
    res.status(404).json({
        status: 'Fail',
        message: `The endpoint ${ req.originalUrl } does not exist`,
    })
})

/*
 * Setup listener and connect to database.
 */
https.createServer({
    key: fs.readFileSync(process.env.KEY),
    cert: fs.readFileSync(process.env.CERT),
}, app).listen(port, async (req, res) => {
    console.log(`Impulse Newsletter back-end system listening on port ${ port }`)
    await connectDb()
})
app.listen(localPort, async (req, res) => {
    console.log(`Localhost listening on port ${ localPort }`)
})