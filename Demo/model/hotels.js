const mongoose = require('mongoose');
// import mongoose, { mongo } from 'mongoose';
// const { Schema } = mongoose;
// var random = require('mongoose-simple-random');

const hotelsSchema = mongoose.Schema({
  ID: String,
  Cluster: String,
  sizeOfCluster: String,
  Website: String,
  City: String,
  name:  String, // String is shorthand for {type: String}
  Url: String,
  address: String,
  Stars: String,
  Price: Number,
  Rating: String,
  number_review: String,
  Reviews: String,
  Facilities: String,
  Description: String,
  Nearby_places: String,
  // Reviews: [String],
  // Facilities: [String],
  // Description: [String],
  // Nearby_places: [String],
  Image: String,
  new_name: String,
  new_add: String
}, {collection: 'data_integration', timestamps: true});

// productsSchema.plugin(random);

module.exports = mongoose.model('hotels', hotelsSchema);