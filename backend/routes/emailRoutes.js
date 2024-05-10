const express = require("express");
const router = express.Router();
const emailController = require("../controllers/emailController");

router.get("/all", emailController.getAllEmails);
router.get("/", emailController.doesEmailExist);
router.post("/", emailController.addEmail);
router.post("/:email", emailController.removeEmail);

module.exports = router;