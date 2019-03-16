const Discord = require('discord.js')
const client = new Discord.Client()
const https = require('https');
const fs = require('fs');

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})

client.on('message', (receivedMessage) => {

    if (receivedMessage.author == client.user) {
        return
    }

    const year = getYearNum()
    const week = getNumberOfWeek()
    const directory = createWeekDirIfNotExists("w" + week + "y" + year)

    if(receivedMessage.attachments.first()){
        if(receivedMessage.attachments.first().filename.indexOf('.replay') !== -1){

            const file = fs.createWriteStream(directory + "/" + receivedMessage.author.username + "_" + receivedMessage.attachments.first().filename);
            const request = https.get(receivedMessage.attachments.first().url, function(response) {
                response.pipe(file);
            });

        }else{
            receivedMessage.delete()
        }
    }else{
        receivedMessage.delete()
    }
})

function createWeekDirIfNotExists(dir){

    if (!fs.existsSync(dir)){
        fs.mkdirSync(dir);
    }
    return dir
}

function getYearNum(){
    const today = new Date()
    return today.getFullYear()
}
function getNumberOfWeek() {
    const today = new Date();
    const firstDayOfYear = new Date(today.getFullYear(), 0, 1);
    const pastDaysOfYear = (today - firstDayOfYear) / 86400000;
    return Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7);
}

bot_secret_token = ""

client.login(bot_secret_token)