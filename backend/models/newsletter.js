const { DataTypes } = require("sequelize");
const { sequelize } = require('../database/sequelize');

module.exports = sequelize.define('Newsletter', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    title: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    content: {
        type: DataTypes.TEXT,
        allowNull: false,
    },
    image: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    posted: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
    },
});