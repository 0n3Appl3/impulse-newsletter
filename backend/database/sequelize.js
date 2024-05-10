const dotenv = require('dotenv').config({
    path: '../.env',
})
const { Sequelize } = require('sequelize');

/*
 * Create new instance of Sequelize.
 */
const sequelize = new Sequelize(
    process.env.DB_NAME, 
    process.env.DB_USER, 
    process.env.DB_PASSWORD,
    {
        host: process.env.DB_HOST,
        dialect: 'mysql',
        define: {
            freezeTableName: true,
            timestamps: false,
        }
    }
);

/*
 * Establish a connection to the MySQL database.
 */
const connectDb = async () => {
    try {
        await sequelize.authenticate();
        await sequelize.sync()
        console.log('Connection has been established successfully.');
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
}

module.exports = {
    sequelize,
    connectDb
};