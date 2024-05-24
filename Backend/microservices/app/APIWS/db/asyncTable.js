'use strict';

const EventEmitter = require('events');
const r = require('rethinkdb');
const database = require('./database');

/**
 * Clase para manejar la escucha de cambios asincrónicos en una tabla de RethinkDB.
 * @extends EventEmitter
 */
class AsyncTable extends EventEmitter {

    /**
     * Crea una instancia de AsyncTable.
     * @param {string} tableName El nombre de la tabla a escuchar.
     */
    constructor(tableName) {
        super();
        /**
         * El nombre de la tabla.
         * @type {string}
         */
        this.tableName = tableName;
    }

    /**
     * Inicia la escucha de cambios en la tabla especificada.
     * @returns {Promise<void>} Una promesa que se resuelve cuando se inicia la escucha de cambios.
     */
    async start() {
        try {
            const connection = database.getConnection();
            /**
             * Cursor que representa la secuencia de cambios en la tabla.
             * @type {import('rethinkdb').Cursor}
             */
            const cursor = await r.table(this.tableName).changes().run(connection);
            cursor.each((err, row) => {
                if (err) throw err;
                /**
                 * Evento que se emite cuando hay un cambio en la tabla.
                 * @event AsyncTable#change
                 * @type {Object}
                 */
                this.emit('change', row);
            });
        } catch (err) {
            console.error('Error al iniciar feed de la tabla:', err);
        }
    }
}

module.exports = AsyncTable;
