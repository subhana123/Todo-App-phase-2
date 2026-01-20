import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      // Proxy API requests to the backend server
      {
        source: "/api/:path*",
        destination: "http://localhost:8000/api/v1/:path*", // Proxy to backend
      },
    ];
  },
};

export default nextConfig;
