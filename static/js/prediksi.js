document.addEventListener("DOMContentLoaded", function () {
    const sayuran = document.querySelectorAll(".sayuran.selectable");
    let selectedSayuran = null;

    sayuran.forEach((item) => {
        item.addEventListener("click", function () {
            if (selectedSayuran) {
                selectedSayuran.classList.remove("border-2", "border-primary");
            }
            selectedSayuran = item;
            selectedSayuran.classList.add("border-2", "border-primary");
        });
    });

    const predictButton = document.getElementById("predict");
    predictButton.addEventListener("click", function () {
        if (!selectedSayuran) {
            alert("Pilih sayuran terlebih dahulu!");
            return;
        }
        const sayuranId = selectedSayuran.id;
        const cuaca = document.getElementById("cuaca").value;
        const suhu = document.getElementById("suhu").value;
        const lokasi = document.getElementById("lokasi").value;
        const tanah = document.getElementById("tanah").value;

        axios
            .post("/predict", {
                sayuran: sayuranId,
                cuaca: cuaca,
                suhu: suhu,
                lokasi: lokasi,
                tanah: tanah,
            })
            .then(function (response) {
                const resultSection = document.getElementById("result");
                const resultMessage = document.getElementById("result-message");
                resultSection.classList.remove("hidden");

                if (response.data.success) {
                    resultMessage.innerHTML =
                        "<h1 class='text-3xl font-bold text-green-500'>Prediksi Sukses!</h1><p class='mt-4 text-lg text-gray-700'>Selamat! Kondisi tanaman Anda ideal untuk pertumbuhan yang optimal.</p><a href='/templates/sukses.html' class='text-blue-500 underline'>Lihat Selengkapnya</a>";
                } else {
                    resultMessage.innerHTML =
                        "<h1 class='text-3xl font-bold text-red-500'>Prediksi Gagal</h1><p class='mt-4 text-lg text-gray-700'>Maaf, kondisi tanaman Anda kurang ideal untuk pertumbuhan yang optimal.</p><a href='/templates/gagal.html' class='text-blue-500 underline'>Lihat Selengkapnya</a>";
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    });
});