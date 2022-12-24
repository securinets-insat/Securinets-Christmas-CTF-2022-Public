const form = document.getElementById("form");

form.addEventListener("submit", submitForm);
const resultTag = document.getElementById("result");

async function submitForm(e) {
  e.preventDefault();
  const name = document.getElementById("name");
  const files = document.getElementById("files");
  const formData = new FormData();
  formData.append("name", name.value);
  for (let i = 0; i < files.files.length; i++) {
    formData.append("files", files.files[i]);
  }

  try {
    const res = await fetch("/upload_files", {
      method: "POST",
      body: formData,
    });
    const resBody = await res.json();
    console.log(resBody);

    if (resBody.type === "success") {
      resultTag.innerHTML = `
      <div class="p-4 mb-4 text-sm text-green-700 bg-green-100 rounded-lg dark:bg-green-200 dark:text-green-800" role="alert">
  <span class="font-medium">Thanks for not trying to pwn my server 😏 </span> Chang a few things up and try submitting again.
</div>
      <div class='success'></div>`;
    } else if (resBody.type === "error") {
      resultTag.innerHTML = `<div class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg dark:bg-red-200 dark:text-red-800" role="alert">
  <span class="font-medium">${resBody?.message}. </span>Change a few things up and try submitting again.
</div>`;
    } else if (resBody.type === "pwned") {
      resultTag.innerHTML = `<div class="p-4 mb-4 text-sm text-yellow-700 bg-yellow-100 rounded-lg dark:bg-yellow-200 dark:text-yellow-800" role="alert">
  <span class="font-medium">Congratulations, here is your flag</span><span class='text-orange-800'> ${resBody?.message} </span>
</div>`;
    }
    setTimeout(() => {
      resultTag.innerHTML = "";
    }, 15000);
  } catch (err) {
    console.log("Error occured", err);
  }
}
