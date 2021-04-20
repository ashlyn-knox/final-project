const express = require('express')
const mongoose = require('../../_connection')
const formModel = require('../../models/form')

const router = express.Router()

router.get('/api/form', async (req, res) => {
  try {
    const formCollection = await Form.Find({})
    res.json(formCollection)
  } catch (err) {
    res.sendStatus(404)
  }
})

module.exports = router
