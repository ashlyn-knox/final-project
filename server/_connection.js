const mongoose = require('mongoose')
const dotenv = require('dotenv').config()

mongoose.connect(
  process.env.MONGODB_URL,
  { useUnifiedTopology: true, useNewUrlParser: true }
)
  .then(() => {
    console.log('Connected to DB...')
  })
  .catch((err) => {
    console.log(`${err} Internal Server Error`)
  })

module.exports = mongoose;
