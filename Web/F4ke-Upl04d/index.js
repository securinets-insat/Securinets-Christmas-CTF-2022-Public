const express = require("express");
const multer = require("multer");
const upload = multer({ dest: "uploads/" });
var fs = require("fs");
var Buffer = require("buffer").Buffer;
const nunjucks = require("nunjucks")
const path = require("path")
const dotenv = require("dotenv")

dotenv.config();

const app = express();
nunjucks.configure({ autoescape: true });
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(bodyParser())

app.use(express.static("public"));

app.post("/upload_files", upload.array("files"), uploadFiles);

const ALLOWED_FILES_TYPES = ["ffd8ffe0", "ffd8ffe1", "89504e47", "47494638"];

async function uploadFiles(req, res) {
  console.log(req.files);

  if (req.files.length === 0)
    return res.status(400).json({ message: "You should upload a file !", type: "error" });

  if (req.files.length > 1)
    return res.status(400).json({
      message: "You should upload only one file",
      type: "error",
    });

  if (
    !req.files[0].originalname.endsWith(".jpg") &&
    !req.files[0].originalname.endsWith(".png") &&
    !req.files[0].originalname.endsWith(".gif")
  )
    return res.status(400).json({
      message: "Make sure you uploaded a picture in a .png/.jpg format",
      type: "error",
    });

  let check = false;
  try {
    const fd = fs.openSync(path.join(process.cwd(), req.files[0].path), "r",);
    if (fd > 0) {
      console.log(req.files[0].path)
      var buffer = new Buffer(30);
      const numbersOfBytesRead = fs.readSync(fd, buffer, 0, 30, 0);

      if (numbersOfBytesRead <= 0) { return res.json({ message: "Broken again", type: "error" }) }

      const magicNumber = buffer.toString("hex", 0, 4);

      if (ALLOWED_FILES_TYPES.includes(magicNumber)) {
        check = true;
      }
      else {
        try {
          fs.rmSync(req.files[0].path)
        }
        catch (error) { }
      }
      fs.closeSync(fd)
    }

    if (check) {
      try {
        const file_content = fs.readFileSync(req.files[0].path, "utf-8")
        console.log(file_content)
        try {
          const rendered = nunjucks.renderString(file_content)
          fs.rmSync(req.files[0].path);
          return res.status(200).send(rendered);
        }
        catch (error) {
          return res.json({
            message: " Broke it again aghh",
            type: 'error'
          })
        }
      }
      catch (error) {
        console.log(error)
        return res.status(500).json({
          message: "Error has occurred. Now you broke it nice hacker !",
          type: "error"
        })
      }

    }
    else {
      return res.json({
        message: "Play by rules you boi",
        type: 'error'
      })
    }
  }
  catch (error) {
    console.log(error)
    return res.json({
      type: "error",
      message: "Error occurred while uploading the file"
    })
  }

}


app.get("/ping", (req, res) => {
  return res.json({ message: "pong" });
});

app.listen(process.env.PORT, () => {
  console.log(`Server started...`);
});
