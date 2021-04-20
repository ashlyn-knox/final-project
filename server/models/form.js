const mongoose = require('mongoose')
const formSchema = new mongoose.Schema(
  {
  name: String,
  age: Number
}
)

module.exports = mongoose.model('Form', formSchema)
