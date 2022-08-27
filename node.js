express = require('express')
const app = express()
const port = process.env.PORT || 3000
const fs = require('fs');


app.get('/', (req, res) => {
    res.send('Hello World!')
  })
app.get("/data/:id", (req,res) => {
    const id =req.params.id
    console.log('--------')
    fs.readFile('./file.csv', 'utf8', (err, data) => {
        const line = data.split('\n')[id]
        if (err) {
          console.error(err);
          return;
        }
        const vetor = line.split(',')
        for (let i=0;i < vetor.length;i++){
            vetor[i] = Number(vetor[i])
        }
        res.send({data: vetor})
      });
})
  
  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
  })