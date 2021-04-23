const express = require('express')
const formCollection = require('./api/form')
const formData = require('../models/form')
const request = require('request')
const router = express.Router()

router.use(express.urlencoded({extended: true}))

// home route TODO set to vue
router.get('/', (req, res) => {
  res.send('node home')
})

// Connect to flask server TODO send form data to this
router.get('/flask', (req, res) => {
  request('http://127.0.0.1:5000/flask', (error, response, body) => {
    console.log('error:', error)
    console.log('statusCode:', response && response.statusCode)
    console.log('body:', body)
    res.send(body)
  })
})

// TODO integrate with flask server
router.post('/form', async (req, res, next) => {
  try {
    const formItem = new formData(req.body)
    formItem.save((err, data) => {
      if (err) {
        res.send(`<p>${err} Problem creating form entry</p>`)
      }
      res.send(`<p>Created form Entry</p>`)
    })
  }catch (err) {
    res.sendStatus(404)
  }
})

// Normal Routes


module.exports = router
