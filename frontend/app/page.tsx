"use client";

import { useState, useRef, useEffect } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const replyRef = useRef<HTMLDivElement>(null);

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = textareaRef.current.scrollHeight + "px";
    }
  }, [message]);

  // Scroll to reply when it appears
  useEffect(() => {
    if (reply && replyRef.current) {
      replyRef.current.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }, [reply]);

  async function send() {
    const trimmedMessage = message.trim();
    if (!trimmedMessage) {
      setError("Please enter a message");
      return;
    }

    setIsLoading(true);
    setReply("");
    setError(null);

    try {
      const payload = {
        session_id: "user-001",
        message: trimmedMessage,
      };

      const apiUrl = process.env.NEXT_PUBLIC_API_URL;
      if (!apiUrl) {
        throw new Error("API URL is not configured");
      }

      const response = await fetch(`${apiUrl}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        let errorMessage = `Server error: ${response.status}`;
        try {
          const errorData = await response.json();
          if (errorData.message) {
            errorMessage = errorData.message;
          }
        } catch (e) {
          // If response isn't JSON, use status text
          if (response.statusText) {
            errorMessage = `${response.status}: ${response.statusText}`;
          }
        }
        throw new Error(errorMessage);
      }

      if (!response.body) return;

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");
      
    while (true) {
    const { value, done } = await reader.read();

    if (done) break;

    const chunk = decoder.decode(value);

    setReply((prev) => prev + chunk);
  }

    } catch (error) {
      console.error("Chat Error:", error);
      const errorMessage = error instanceof Error ? error.message : "Failed to connect to the Travel Planner API. Please try again.";
      setError(errorMessage);
      setReply(""); // Clear any partial reply
    } finally {
      setIsLoading(false);
    }
  }

  function handleKeyDown(e: React.KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  }

  function clearChat() {
    setMessage("");
    setReply("");
    setError(null);
    if (textareaRef.current) {
      textareaRef.current.focus();
    }
  }

  return (
    <main className="max-w-3xl mx-auto p-4 sm:p-6 md:p-10 space-y-4 sm:space-y-6 min-h-screen">
      {/* Header */}
      <div className="flex items-center justify-between">
        <h1 className="text-3xl sm:text-4xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          🌍 Travel Planner AI
        </h1>
        <button
          onClick={clearChat}
          className="text-sm text-gray-500 hover:text-gray-700 transition-colors"
          aria-label="Clear chat"
        >
          Clear Chat
        </button>
      </div>

      <p className="text-gray-600 text-sm sm:text-base">
        Ask me about destinations, flights, hotels, and more!
      </p>

      {/* Error Message */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-red-700 flex items-start gap-3">
          <span className="text-lg" aria-hidden="true">⚠️</span>
          <div className="flex-1">
            <p className="font-semibold">Error</p>
            <p className="text-sm">{error}</p>
          </div>
          <button
            onClick={() => setError(null)}
            className="text-red-500 hover:text-red-700 text-sm font-medium"
            aria-label="Dismiss error"
          >
            Dismiss
          </button>
        </div>
      )}

      {/* Input Area */}
      <div className="space-y-3">
        <div className="relative">
          <textarea
            ref={textareaRef}
            className="w-full border rounded-lg p-4 pr-12 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-shadow resize-none min-h-[120px] text-sm sm:text-base"
            rows={4}
            placeholder="Where would you like to travel next? e.g., 'I want to visit Paris for 5 days'"
            value={message}
            onChange={(e) => {
              setMessage(e.target.value);
              if (error) setError(null);
            }}
            onKeyDown={handleKeyDown}
            disabled={isLoading}
            aria-label="Travel message"
          />
          
          {/* Character count */}
          <div className="absolute bottom-3 right-3 text-xs text-gray-400">
            {message.length} characters
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-3 sm:gap-4">
          <button
            onClick={send}
            disabled={isLoading || !message.trim()}
            className={`flex-1 bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-3 rounded-lg font-medium transition-all ${
              isLoading || !message.trim()
                ? "opacity-50 cursor-not-allowed"
                : "hover:shadow-lg hover:scale-[1.02] active:scale-[0.98]"
            }`}
          >
            {isLoading ? (
              <span className="flex items-center justify-center gap-2">
                <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Thinking...
              </span>
            ) : (
              "✈️ Ask AI"
            )}
          </button>
          
          <button
            onClick={() => {
              setMessage("");
              if (textareaRef.current) {
                textareaRef.current.focus();
              }
            }}
            disabled={isLoading || !message}
            className={`px-4 py-3 rounded-lg border transition-colors ${
              isLoading || !message
                ? "opacity-50 cursor-not-allowed bg-gray-50"
                : "hover:bg-gray-50"
            }`}
            aria-label="Clear input"
          >
            Clear
          </button>
        </div>

        {/* Keyboard shortcut hint */}
        <p className="text-xs text-gray-400 text-center">
          Press <kbd className="px-1 py-0.5 bg-gray-100 rounded border text-xs font-mono">Enter</kbd> to send,{' '}
          <kbd className="px-1 py-0.5 bg-gray-100 rounded border text-xs font-mono">Shift + Enter</kbd> for new line
        </p>
      </div>

      {/* Reply Area */}
      {reply && (
        <div 
          ref={replyRef}
          className="border-2 border-blue-100 rounded-lg p-5 sm:p-6 bg-gradient-to-br from-blue-50 to-purple-50 animate-fadeIn"
        >
          <div className="flex items-start gap-3">
            <span className="text-2xl" aria-hidden="true">🤖</span>
            <div className="flex-1">
              <h2 className="font-semibold text-gray-700 mb-2 text-sm uppercase tracking-wide">
                AI Travel Assistant
              </h2>
              <div className="prose prose-sm sm:prose-base max-w-none whitespace-pre-wrap text-gray-800 leading-relaxed">
                {reply}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Loading Skeleton (optional) */}
      {isLoading && !reply && (
        <div className="border rounded-lg p-5 bg-gray-50 animate-pulse">
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 bg-gray-300 rounded-full"></div>
            <div className="flex-1 space-y-3">
              <div className="h-4 bg-gray-300 rounded w-3/4"></div>
              <div className="h-4 bg-gray-300 rounded w-1/2"></div>
              <div className="h-4 bg-gray-300 rounded w-5/6"></div>
            </div>
          </div>
        </div>
      )}

      {/* Empty State */}
      {!reply && !isLoading && !error && (
        <div className="text-center py-12 text-gray-400 border-2 border-dashed rounded-lg">
          <p className="text-6xl mb-4" aria-hidden="true">🗺️</p>
          <p className="font-medium">Ready to plan your next adventure!</p>
          <p className="text-sm mt-1">Ask me anything about travel destinations</p>
        </div>
      )}

      {/* Hidden div for CSS animation */}
      <style jsx>{`
        @keyframes fadeIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-fadeIn {
          animation: fadeIn 0.3s ease-out;
        }
      `}</style>
    </main>
  );
}