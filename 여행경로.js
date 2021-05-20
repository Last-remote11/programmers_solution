function solution(tickets) {

  let answer = []
  let queue = [] // [현재위치, 남은티켓, 지나온 공항들]
  answer.push('ICN')

  let filtered = tickets.filter(e => e[0] === 'ICN').sort((a, b) => {
    if (a[1].charCodeAt(0) > b[1].charCodeAt(0)) return -1
    if (a[1].charCodeAt(0) < b[1].charCodeAt(0)) return 1
    if (a[1].charCodeAt(1) > b[1].charCodeAt(1)) return -1
    if (a[1].charCodeAt(1) < b[1].charCodeAt(1)) return 1
    if (a[1].charCodeAt(2) > b[1].charCodeAt(2)) return -1
    if (a[1].charCodeAt(2) < b[1].charCodeAt(2)) return 1
  })

  for (let i of filtered) {
    let idx = tickets.indexOf(i)
    let nextAns = [...answer]
    nextAns.push(i[1])
    queue.push([i[1], tickets.slice(0, idx).concat(tickets.slice(idx+1)), nextAns])
  }
    
    // let current = filtered[0]

  while (queue.length != 0) {
    let [cur, tickets, ans] = queue.pop()
    if (tickets.length === 0) {
      return ans
    }
    let filtered2 = tickets.filter(e => e[0] === cur).sort((a, b) => {
      if (a[1].charCodeAt(0) > b[1].charCodeAt(0)) return -1
      if (a[1].charCodeAt(0) < b[1].charCodeAt(0)) return 1
      if (a[1].charCodeAt(1) > b[1].charCodeAt(1)) return -1
      if (a[1].charCodeAt(1) < b[1].charCodeAt(1)) return 1
      if (a[1].charCodeAt(2) > b[1].charCodeAt(2)) return -1
      if (a[1].charCodeAt(2) < b[1].charCodeAt(2)) return 1
    })
    if (filtered2.length === 0) { continue }
    for (let next of filtered2) {
      let idx = tickets.indexOf(next)
      let nextAns = [...ans]
      nextAns.push(next[1])
      queue.push([next[1], tickets.slice(0, idx).concat(tickets.slice(idx+1)), nextAns])
    }
  }
 

  return answer
}
