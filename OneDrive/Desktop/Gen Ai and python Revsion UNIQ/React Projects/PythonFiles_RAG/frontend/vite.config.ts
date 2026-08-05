import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/

export default defineConfig({

    plugins: [

        react()

    ],

    server: {

        port: 5173,

        open: true,

        proxy: {

            "/auth": {

                target: "http://localhost:8000",

                changeOrigin: true

            },

            "/upload": {

                target: "http://localhost:8000",

                changeOrigin: true

            },

            "/screen": {

                target: "http://localhost:8000",

                changeOrigin: true

            },

            "/report": {

                target: "http://localhost:8000",

                changeOrigin: true

            }

        }

    }

});