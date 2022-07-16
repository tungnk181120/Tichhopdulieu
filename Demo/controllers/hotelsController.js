var productsModel = require('../model/hotels.js')

class HotelsController{
    index(req, res){
        // productsModel.findOne({}, function(err, data){
        //     res.render('product', { title: 'product', dulieu:data});
        //     // console.log(data.colors);
        //   })
        res.send("product")
    };
    show(req, res, next){
        // productsModel.findOne({name: req.params.name})
        // .then((product) => {
        //     res.json(product)
        // })
        // productsModel.findRandom({}, {}, {limit: 4}, function(err, result){
        //         res.send(result);
        // })
        // .catch(next);
        //var product, recommendproduct;
        Promise.all([productsModel.findOne({name: req.params.name}), 
            productsModel.findRandom({}, {}, {limit: 4}, function(err, result){
                return result;
            })])
            .then(([productinfo, recommendproduct]) =>
                res.render('user/product', {
                    title: req.params.name,
                    product: productinfo,
                    productRecommends: recommendproduct
            })
            )
            .catch(next);

    // res.send(req.params.name);
    };
    showColor(req, res, next){
        Promise.all([productsModel.findOne({name: req.params.name}), 
            productsModel.findRandom({}, {}, {limit: 4}, function(err, result){
                return result;
            })])
            .then(([productinfo, recommendproduct]) =>
                res.render('product', {
                    title: req.params.name,
                    product: productinfo,
                    productRecommends: recommendproduct
            })
            )
            .catch(next);
    }

}
module.exports = new HotelsController;