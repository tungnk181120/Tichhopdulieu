const { query } = require('express');
var express = require('express');
const hotels = require('../model/hotels.js');
var router = express.Router();
var hotelsModel = require('../model/hotels.js')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Hotel Integration' });
});
// router.get('/search_result', function(req, res, next) {
//   // res.send(req.query.search-query)
//   res.render('search_result', { title: 'Search Result' });
// });

// Search engine
router.get('/search_result', function(req, res, next) {
  // Product.find({
  //   name: {
  //     "$regex": req.query.search-query,
  //   }, function(err, products){
  //     res.render('user/search', { title: 'Search results', products: products })
  //   }
  // })
  hotelsModel.find({City: req.query.searchname}).exec( function(err, hotels){
    res.render('search_result', {title: "Search results", hotels:hotels})
  })
  //res.send(req.query.search-query)
});


// router.get('/hotel', function(req, res, next) {
//   res.render('hotel', { title: 'Hotel' });
// });
router.get('/hotel/:cluster', function(req, res, next) {
  // hotelsModel.find({ $or: [{ Cluster: req.params.cluster}] }, function(err, hotels){
  //   res.render('hotel', {title: "Search results", hotel:hotels[0], hotel1:hotels[1]})
  // })
  // <% numberOfHotel = hotels.length; %>
  //   <% if(numberOfHotel == 1){ %>
  //       <% hotel = hotels; %>
  //   <% } else if (numberOfHotel === 2) { %>
  //       <%  %>
  //   <% } else{ %>  
  //   <% } %>

  // <% Facilities = hotel.Facilities;%>
  // <% Facilities.forEach(function(facility){ %>
  //     <span class="facility"><%- facility %></span>
  // <% }); %>

  // <% Nearby_places = hotel.Nearby_places;%>
  // <% Nearby_places.forEach(function(place){ %>
  //     <span class="place"><%- place %></span>
  // <% }); %>

  // hotelsModel.find({'Cluster': req.params.cluster}), function(err, hotels){
  //     res.render('hotel', {title: "Search results", hotel:hotels[0]})
  hotelsModel.find({Cluster: req.params.cluster}).sort({Price: 1}).exec(function(err, hotels){
  res.render('hotel', {title: "Search results", hotels:hotels, hotel:hotels[0], hotel1: hotels[1], hotel2:hotels[2], hotel3:hotels[3]})
})
});
module.exports = router;
