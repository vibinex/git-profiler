const express = require ('express');
const router = express.Router();

router.post('/profile', (req, res, next) => {
	// TODO: complete profile extraction logic here
	return res.json("Success")
});

module.exports = router;