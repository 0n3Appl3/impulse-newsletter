const express = require("express");
const router = express.Router();
const newletterController = require("../controllers/newsletterController");

router.post("/", newletterController.addNewsletter);
router.get("/set/posted", newletterController.setNewsletterPosted);
router.get("/", newletterController.getOldestUnpostedNewsletter);

module.exports = router;