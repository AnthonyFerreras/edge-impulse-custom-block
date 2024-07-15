class Block {
    constructor() {
        this.sensitivity = 1;
    }

    init() {
        // Initialization logic here
        console.log('Block initialized');
    }

    configure(params) {
        // Set sensitivity from user parameters
        this.sensitivity = params.sensitivity;
        console.log('Sensitivity set to:', this.sensitivity);
    }

    start() {
        // Logic to start data processing
        console.log('Processing started');
    }

    process(signal, length, context) {
        // Apply sensitivity adjustment
        let adjustedSignal = signal.map(x => x * this.sensitivity);
        console.log('Signal processed');
        return adjustedSignal;
    }

    clean() {
        // Clean up resources if needed
        console.log('Clean up');
    }
}

module.exports = Block;