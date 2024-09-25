import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client
  .on("connect", () => {
    console.log("Redis client connected to the server");
  })
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

asyncGet = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    const value = await asyncGet(schoolName).catch((error) => {
      if (error) {
        console.log(error);
        throw error;
      }
    });
    console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
