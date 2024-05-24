// database.js

'use strict';

const r = require('rethinkdb');


/**
 * Clase para manejar la conexión a la base de datos RethinkDB.
 */
class Database {


    /**
     * Crea una instancia de Database
     */
    constructor() {
        /**
         * La conexión actual a la base de datos
         * @type {import('rethinkdb').Connection | null}
         */
        this.connection = null;
    }

    /**
     * Conexta a la base de datos RethinkDB
     * @returns {Promise<void>} Una promesa que se devuelve cuando se establece la conexión a la DB.
     */
    async connect() {

        try {
            this.connection = await r.connect({
                host: 'localhost',
                port: 28015,
                db: 'test'
            });
            console.log('Conectado a RethinkDB');

        } catch (err) {
            console.error('Error al conectar a RethinkDB:', err)
        }
    }

    /**
     * 
     * @returns Instancia de la clase Database, lista para ser exportada.
     * @type {Database}
     */
    getConnection() {
        return this.connection;
    }
}


module.exports = new Database();