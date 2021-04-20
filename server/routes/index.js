const express = require('express')
const formCollection = require('./api/form')
const formData = require('../models/form')
const router = express.Router()

router.use(express.urlencoded({extended: true}))

// form middleware
// post form TODO review fcc tutorial
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

module.exports = router
