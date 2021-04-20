const mongoose = require('./_connection')

const dbSeed = require('./seeds/formStorage')

const formModel = require('./models/form')

formModel.insertMany(dbSeed, (err, form) => {
  if (err) {
    console.log(err)
  }
  console.log('Data Import Complete.')
  mongoose.connection.close()
})
