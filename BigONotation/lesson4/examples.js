function logFunc(n) {
    if (n === 0) return "Done";
    n = Math.floor(n/2);
    return logFunc(n);
}

logFunc(8)