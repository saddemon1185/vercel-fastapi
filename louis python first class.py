{
    "version": 2,
    "builds": [
        {
            "src": "src/server.ts",
            "use": "@vercel/node"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "src/server.ts"
        }
    ]
}