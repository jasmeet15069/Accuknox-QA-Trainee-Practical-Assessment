const express = require('express');
const axios = require('axios');
const winston = require('winston');

const app = express();
const PORT = process.env.PORT || 3000;

// Set up logging
const logger = winston.createLogger({
    format: winston.format.json(),
    transports: [
        new winston.transports.File({ filename: 'application_health.log' }),
        new winston.transports.Console()
    ],
});

// Health check endpoint
app.get('/check_health', async (req, res) => {
    const url = req.query.url;

    if (!url) {
        return res.status(400).json({ error: "No URL provided" });
    }

    try {
        const response = await axios.get(url, { timeout: 10000 }); // 10 seconds timeout
        if (response.status === 200) {
            logger.info(`Application is up and running: ${url}`);
            return res.status(200).json({ status: "up", url });
        } else {
            logger.warn(`Application is down or not responding: ${url} - Status Code: ${response.status}`);
            return res.status(response.status).json({ status: "down", url, status_code: response.status });
        }
    } catch (error) {
        logger.error(`Error checking application health: ${error.message}`);
        return res.status(500).json({ status: "error", message: error.message });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
