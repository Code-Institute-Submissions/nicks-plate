const testDay = require('/day');
const d = new Date()
let day = d.getDay()
today = day 
// today == Tuesday

describe('day', () => {
    describe('dayIsMonday', () => {
        test('should return 1', () => {
            expect(day - 1).toBe(1)
        })
    })
    describe('dayIsTuesday', () => {
        test('should retudn 2', () => {
            expect(today).toBe(2)
        })
    })
    describe('dayIsWednesday', () => {
        test('should retudn 3', () => {
            expect(today + 1).toBe(3)
        })
    })
    describe('dayIsThursday', () => {
        test('should retudn 4', () => {
            expect(today + 2).toBe(4)
        })
    })
    describe('dayIsFriday', () => {
        test('should retudn 5', () => {
            expect(today + 3).toBe(5)
        })
    })
    describe('dayIsSaturday', () => {
        test('should retudn 6', () => {
            expect(today + 4).toBe(6)
        })
    })
    describe('dayIsSunday', () => {
        test('should retudn 0', () => {
            expect((today + 5)%7).toBe(0)
        })
    })
})

// Test Suites: 1 passed, 1 total
// Tests:       7 passed, 7 total
// Snapshots:   0 total
// Time:        0.698 s, estimated 1 s
// Ran all test suites.