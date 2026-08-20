<?php
/*
Plugin Name: developer-assesment-products
Description: This plugin add a products to WordPress.
Version: 1.0
Author: mahdi
*/


if ( ! defined( 'ABSPATH' ) ) {
    exit; // Exit if accessed directly
}

add_action( 'init', 'product_registeration' );
function product_registeration() {
    $args = array(
        'labels' => array(
            'name'          => 'products',
            'singular_name' => 'product',
            'menu_name'     => 'products',
            'add_new'       => 'Add New Product',
            'add_new_item'  => 'Add New Product',
            'new_item'      => 'New Product',
            'edit_item'     => 'Edit Product',
            'view_item'     => 'View Product',
            'all_items'     => 'All Product',
        ),
        'public' => true,
        'has_archive' => true,
        'show_in_rest' => true,
        'supports' => array( 'title', 'description', 'author', 'thumbnail', 'excerpt', 'sku', 'quantity', 'price' ),
    );

    register_post_type( 'product', $args );
}