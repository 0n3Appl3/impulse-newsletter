const Newsletter = require('../models/newsletter');

exports.addNewsletter = async (req, res) => {
    try {
        const newsletter = await Newsletter.create({
            title: req.body.title,
            content: req.body.content,
            image: req.body.image,
            posted: false,
        })
        res.status(201).json({
            status: 'Created',
            message: 'Newsletter added successfully'
        })
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
};

exports.setNewsletterPosted = async (req, res) => {
    try {
        const newsletter = await Newsletter.findOne({
            where: {
                posted: false,
            }
        })
        if (!newsletter) {
            return res.status(404).json({
                status: 'Fail',
                message: 'No unposted newsletter found to set as posted'
            })
        }
        newsletter.posted = true
        await newsletter.save()
        res.status(200).json({
            status: 'Created',
            message: 'Newsletter set as posted successfully'
        })
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
}

exports.getOldestUnpostedNewsletter = async (req, res) => {
    try {
        const newsletter = await Newsletter.findOne({
            where: {
                posted: false,
            }
        })
        if (!newsletter) {
            return res.status(404).json({
                status: 'Fail',
                message: 'No unposted newsletter found'
            })
        }
        res.status(200).json(newsletter)
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
}