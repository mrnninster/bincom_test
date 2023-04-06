
const lgas = document.getElementById('lgas')

lgas.addEventListener("change", () => {
    
    const xhr = new XMLHttpRequest()
    xhr.open("GET",`/pu_listings/${lgas.value}`, true)
    xhr.send()
    xhr.onload = () => {
        const response = JSON.parse(xhr.responseText)
        const pole_count = document.getElementById('pole_count')
        pole_count.innerText = response["pole_sum"]
    }
})