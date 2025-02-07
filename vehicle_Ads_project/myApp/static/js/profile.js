const deletebtn = document.querySelectorAll(".deletebtn");

Array.from(deletebtn).forEach((btn) => {
  btn.addEventListener("click", function (e) {
    e.preventDefault();
    const deleteUrl = this.getAttribute("href");
    Swal.fire({
      title: "Do you want to delete the<br> your post?",
      text: "",
      showCancelButton: true,
      confirmButtonColor: "#dc3545",
      cancelButtonColor: "#28a745",
      confirmButtonText: "Delete!",
      cancelButtonText: "Cancel",
      background: "#f8f9fa",
      customClass: {
        title: "text-success",
        cancelButton: "btn btn-secondary",
        confirmButton: "btn btn-danger",
        popup: "rounded-3 shadow-lg",
        content: "fs-5",
      },
    }).then((result) => {
      if (result.isConfirmed) {
        fetch(deleteUrl).then((res) => {
          if (res.ok) {
            Swal.fire({
              title: "Deleted!",
              text: "Your post has been deleted.",
              icon: "success",
              confirmButtonText: "OK",
              confirmButtonColor: "#28a745",
              background: "#e9ecef",
              customClass: {
                title: "text-success",
                confirmButton: "btn btn-success",
              },
            }).then(() => {
              location.reload();
            });
          }
        });
      }
    });
  });
});

document.getElementById("deleteuser").addEventListener("click", (e) => {
  e.preventDefault();
  const deleteUrl = document.getElementById("deleteuser").getAttribute("href");
  Swal.fire({
    title: "Do you want to delete the<br> Your Account?",
    text: "If you delete your account, delete all your posts",
    showCancelButton: true,
    confirmButtonColor: "#dc3545",
    cancelButtonColor: "#28a745",
    confirmButtonText: "Delete!",
    cancelButtonText: "Cancel",
    background: "#f8f9fa",
    customClass: {
      title: "text-success",
      cancelButton: "btn btn-success",
      confirmButton: "btn btn-danger",
      popup: "rounded-3 shadow-lg",
      content: "fs-5",
    },
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(deleteUrl).then((res) => {
        if (res.ok) {
          Swal.fire({
            title: "Deleted!",
            text: "Your post has been deleted.",
            icon: "success",
            confirmButtonText: "OK",
            confirmButtonColor: "#28a745",
            background: "#e9ecef",
            customClass: {
              title: "text-success",
              confirmButton: "btn btn-success",
            },
          }).then(() => {
            location.reload();
          });
        }
      });
    }
  });
});

document.getElementById("logout").addEventListener("click", (e) => {
  e.preventDefault();
  const deleteUrl = document.getElementById("logout").getAttribute("href");
  Swal.fire({
    title: "Do you want to Logout from<br> Your Account?",
    text: "",
    showCancelButton: true,
    confirmButtonColor: "#dc3545",
    cancelButtonColor: "#28a745",
    confirmButtonText: "Logout!",
    cancelButtonText: "Cancel",
    background: "#f8f9fa",
    customClass: {
      title: "text-success",
      cancelButton: "btn btn-success",
      confirmButton: "btn btn-danger",
      popup: "rounded-3 shadow-lg",
      content: "fs-5",
    },
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(deleteUrl).then((res) => {
        if (res.ok) {
          Swal.fire({
            title: "Logout successfully!",
            text: "",
            icon: "success",
            confirmButtonText: "OK",
            confirmButtonColor: "#28a745",
            background: "#e9ecef",
            customClass: {
              title: "text-success",
              confirmButton: "btn btn-success",
            },
          }).then(() => {
            location.reload();
          });
        }
      });
    }
  });
});
