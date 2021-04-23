import { readFileSync } from "fs";

const jsonFromFile = (filename: string): { success: boolean, data: any } => {
  let jsonData = readFileSync(filename);
  let operators = JSON.parse(jsonData.toString());

  return {
    success: true,
    data: operators
  }
};

export default {
  'GET /api/operators': jsonFromFile('./mock/operators.json'),
  'GET /api/costumes': jsonFromFile('./mock/costumes.json')
}
