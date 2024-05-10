const { DataTypes } = require("sequelize");
const { sequelize } = require('../database/sequelize');

module.exports = sequelize.define('Email', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    email: {
        type: DataTypes.STRING,
        allowNull: false,
    },
});