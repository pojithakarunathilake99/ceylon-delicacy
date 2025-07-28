# Ceylon Delicacy - Authentic Sri Lankan Cuisine Restaurant Website

## Overview

This is a website for Ceylon Delicacy, an authentic Sri Lankan cuisine restaurant. The website is built using Flask backend with modern web technologies, featuring responsive design and user experience. It includes a clean, modern design with a warm color palette that reflects the restaurant's brand identity and uses the official Ceylon Delicacy logo with the chef character.

## Recent Changes

### July 28, 2025
- **Authentic Google Reviews Integration**: Replaced placeholder reviews with real customer feedback from Google Maps (5.0★ rating from 5 reviews)
- **Menu Photography**: Added actual food photos for Fish Cutlets, Lamprais, Watalappan, Kokis, and Mung Kavum
- **Menu Expansion**: Added Lamprais as a main course and Mung Kavum as a dessert
- **Business Hours Update**: Updated opening hours to match actual Google Maps listing
- **Direct Google Maps Link**: Added link to view all reviews on Google Maps
- **Events & Catering Section**: Added comprehensive events section showcasing catering services for birthday parties, alms givings, Sri Lankan cultural events, live cooking demonstrations, and corporate events

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Static Website**: Pure HTML, CSS, and JavaScript implementation
- **Framework**: Bootstrap 5.3.0 for responsive grid system and components
- **Font System**: Google Fonts (Poppins) for typography
- **Icons**: Font Awesome 6.4.0 for iconography
- **Styling**: Custom CSS with CSS variables for consistent theming

### Technology Stack
- **HTML5**: Semantic markup structure
- **CSS3**: Custom styling with CSS variables and modern features
- **JavaScript (ES6+)**: Client-side interactivity and animations
- **Bootstrap 5**: Responsive framework for layout and components

## Key Components

### 1. Navigation System
- **Fixed Navigation Bar**: Sticky header with smooth scrolling effects
- **Responsive Design**: Collapsible mobile menu with Bootstrap's navbar component
- **Active State Management**: Dynamic highlighting of current section
- **Smooth Scrolling**: JavaScript-powered smooth navigation between sections

### 2. Visual Design System
- **Color Palette**: 
  - Primary Orange (#FF914D)
  - Secondary Pink (#F56EB3)
  - Dark Text (#4A2C2A)
  - Light Background (#F4F1EE)
- **Typography**: Poppins font family with multiple weights
- **Responsive Layout**: Mobile-first design approach

### 3. Interactive Features
- **Menu Tab System**: JavaScript-powered menu category switching
- **Contact Form**: Client-side form handling and validation
- **Scroll Animations**: Dynamic effects triggered by scroll position
- **Mobile Menu**: Collapsible navigation for mobile devices

## Data Flow

### Client-Side Processing
1. **Page Load**: Initialize all JavaScript modules and event listeners
2. **Scroll Events**: Update navbar styling and active navigation states
3. **User Interactions**: Handle menu tabs, form submissions, and navigation clicks
4. **Animation Triggers**: Activate visual effects based on scroll position

### Navigation Flow
- Single-page application with anchor-based navigation
- Smooth scrolling between sections (Home, Menu, Location, Contact)
- Dynamic active state management for navigation links

## External Dependencies

### CDN Resources
- **Bootstrap 5.3.0**: CSS and JavaScript framework
- **Font Awesome 6.4.0**: Icon library
- **Google Fonts**: Poppins font family
- **External hosting**: All dependencies loaded from CDN for performance

### Asset Dependencies
- **Logo**: PNG format with chef character design (`assets/logo.png`)
- **Custom Styles**: Local CSS file (`css/style.css`)
- **JavaScript**: Local script file (`js/main.js`)

## Deployment Strategy

### Static Website Deployment
- **Hosting**: Can be deployed on any static hosting service (GitHub Pages, Netlify, Vercel, etc.)
- **No Backend Required**: Pure frontend implementation
- **Performance**: Optimized for fast loading with CDN resources
- **SEO**: Basic semantic HTML structure for search engine optimization

### File Structure
```
/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # Custom styles
├── js/
│   └── main.js         # JavaScript functionality
└── assets/
    └── logo.svg        # Restaurant logo
```

### Development Considerations
- **Responsive Design**: Mobile-first approach with Bootstrap grid
- **Cross-Browser Compatibility**: Modern browser support with graceful degradation
- **Performance Optimization**: Minimal custom code, leveraging CDN resources
- **Accessibility**: Semantic HTML structure with proper ARIA attributes

This architecture provides a solid foundation for a restaurant website with room for future enhancements such as online ordering, reservation systems, or content management integration.