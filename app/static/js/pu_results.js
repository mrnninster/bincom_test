
const polling_units = document.getElementById('polling_units')

polling_units.addEventListener("change", () => {
 
        const results = document.querySelectorAll('.result')
        results.forEach(result => {
            result.classList.add("remove_display")
        })

        const unit_poles = document.querySelectorAll(`._${polling_units.value}`)
        unit_poles.forEach(unit_pole => {
            unit_pole.classList.remove("remove_display")
        })

})