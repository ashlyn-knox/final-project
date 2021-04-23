const mongoose = require('mongoose')

const formSchema = new mongoose.Schema({
      python: Boolean,
      javascript: Boolean,
      ruby: Boolean,
      php: Boolean,
      mature: Boolean,
      scalable: Boolean,
      fastDev: Boolean,
      realTime: Boolean,
      machineAi: Boolean,
      microframe: Boolean,
      flexibleData: Boolean,
      structuredData: Boolean
  })

module.exports = mongoose.model('Form', formSchema)
