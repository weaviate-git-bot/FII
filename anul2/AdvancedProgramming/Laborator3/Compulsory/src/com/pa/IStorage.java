package com.pa;

/**
 * An interface that gets the storage capacity of a node in the network
 */
public interface IStorage {
    int getStorageCapacity();

    /**
     * Get the storage capacity in different storage units
     * @param unit the unit you want to get the size in
     * @return the size in specified unit
     */
    default long getStorageCapacityIn(StorageUnits unit) {
        long capacity = getStorageCapacity();
        if(unit == StorageUnits.MEGABYTES)
            return capacity * 1_000;
        if(unit == StorageUnits.KILOBYTES)
            return capacity * 1_000_000;
        if(unit == StorageUnits.BYTE)
            return capacity * 1_000_000_000;
        return capacity;
    }
}
