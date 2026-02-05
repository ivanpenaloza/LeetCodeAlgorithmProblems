class LRUCache {
    private capacity: number;
    private cache: Map<number, number>;

    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map<number, number>();
    }

    get(key: number): number {
        if (!this.cache.has(key)) {
            return -1;
        }
        const value = this.cache.get(key)!;
        // Move to end (most recently used)
        this.cache.delete(key);
        this.cache.set(key, value);
        return value;
    }

    put(key: number, value: number): void {
        // If key exists, delete it first to update position
        if (this.cache.has(key)) {
            this.cache.delete(key);
        }
        this.cache.set(key, value);
        
        // If capacity exceeded, remove the least recently used (first item)
        if (this.cache.size > this.capacity) {
            const firstKey = this.cache.keys().next().value!;
            this.cache.delete(firstKey);
        }
    }
}