import { readFileSync } from 'fs';
import say from 'say';

const SLEEP_TIME_MS = 3000;
const CONFIG_FILE_PATH = 'speaker/is-on';

const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const main = async () => {
    while (true) {
        const { message, shouldSay } = parseConfig();
        if (shouldSay) {
            say.speak(message);
        }

        await sleep(SLEEP_TIME_MS);
    }
}

const parseConfig = () => {
    const data = readFileSync(CONFIG_FILE_PATH, 'utf8');
    const lines = data.split('\n');

    const isOn = lines[0].split(':')[1]?.toLowerCase().includes('true');
    const message = lines[1].split(':')[1];

    return { message, shouldSay: isOn };
}

main();