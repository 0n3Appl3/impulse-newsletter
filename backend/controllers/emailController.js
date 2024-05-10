const Email = require('../models/email');

exports.getAllEmails = async (req, res) => {
    const result = await Email.findAll()

    if (!result) {
        return res.status(404).json({
            status: 'Fail',
            message: 'No results found'
        })
    }
    res.status(200).json(result)
};

exports.doesEmailExist = async (req, res) => {
    try {
        const email = await Email.findOne({
            where: {
                email: req.body.email,
            }
        })
        if (!email) {
            return res.status(404).json({
                status: 'Fail',
                message: 'No results found'
            })
        }
        res.status(200).json({
            status: 'OK',
            message: 'Email exists'
        })
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
}

exports.addEmail = async (req, res) => {
    try {
        const email = await Email.create({
            email: req.body.email
        })
        res.status(201).json({
            status: 'Created',
            message: 'Email added successfully'
        })
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
}

exports.removeEmail = async (req, res) => {
    try {
        const email = await Email.findOne({
            where: {
                email: req.params.email,
            }
        })
        await email.destroy()
        res.status(200).json({
            status: 'OK',
            message: 'Email removed successfully'
        })
    } catch (error) {
        res.status(400).json({
            status: 'Bad Request',
            message: error.message,
        })
    }
}