(() => {
    const locations = {
        STRAIGHT: 'Apple Store',
        LEFT: 'Starbucks',
        RIGHT: 'Science Center',
    }
    const consoleEl = document.querySelector('.console')
    let intervalId = -1

    const getRequestParams = (destination) => ({
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({destination}),
    })

    const formatDirection = direction => {
        switch (direction) {
            case 'LEFT':
                return 'Going left'
            case 'RIGHT':
                return 'Going right'
            case 'STRAIGHT':
                return 'Going straight'
            case 'INTERSECTION':
                return 'Reached an intersection'
            case 'FINISHED':
                return 'Destination reached!'
            default:
                return direction
        }
    }

    const mapLogRow = row => {
        // Return destination name
        if (row.startsWith('DESTINATION')) {
            const destination = locations[row.substring(row.indexOf(' ') + 1)]

            return `Driving to ${destination}`
        } else if (row.startsWith('INTERSECTION '))
            return formatDirection(row.substring(row.indexOf(' ') + 1))
        return formatDirection(row)

    }

    const fetchLog = () => {
        fetch('/log')
            .then(resp => resp.text())
            .then(text => text.split('\n')
                .map(mapLogRow)
                .filter(row => row !== '')
                .join('\n'))
            .then(text => consoleEl.innerHTML = text)
    }

    const buttons = document.querySelectorAll('.destination-list__item--button')
    const onButtonClick = e => {
        const {direction} = e.currentTarget.dataset
        fetch('/start', getRequestParams(direction))
            .then(() => {
                intervalId = setInterval(fetchLog, 2500)
            })
            .catch(err => alert(`unexpected error! ${err}`))
    }
    for (const button of buttons) {
        button.addEventListener('click', onButtonClick)
    }
})()