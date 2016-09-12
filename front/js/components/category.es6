/**
 * Category Page module defines logic, operations and DOM for CategoryPage.
 */
(() => {
  const DOM = {
    $loadedProducts: $('.js-products-showed-count'),
    $productsList: $('#products-wrapper'),
    $viewType: $('#category-right'),
    $loadMore: $('#btn-load-products'),
    $addToCart: $('.js-product-to-cart'),
    tileView: {
      $: $('.js-icon-mode-tile'),
      mode: 'tile',
    },
    listView: {
      $: $('.js-icon-mode-list'),
      mode: 'list',
    },
    $sorting: $('.selectpicker'),
  };

  const config = {
    productsToFetch: 30,
    totalProductsCount: parseInt($('.js-total-products').first().text(), 10),
  };

  const init = () => {
    setUpListeners();
    updateButtonState();
  };

  /**
   * Subscribing on events using mediator.
   */
  function setUpListeners() {
    mediator.subscribe('onViewTypeChange', updateViewType, server.sendViewType);
    mediator.subscribe('onProductsLoad', updateLoadedCount, updateProductsList, updateButtonState);
    DOM.tileView.$.click(() => mediator.publish('onViewTypeChange', DOM.tileView.mode));
    DOM.listView.$.click(() => mediator.publish('onViewTypeChange', DOM.listView.mode));

    DOM.$loadMore.click(loadProducts);
    DOM.$sorting.change(changeSort);
    DOM.$addToCart.click(buyProduct);
  }

  /**
   * Change sorting option and re-renders the whole screen.
   */
  function changeSort() {
    location.href = sortingOption().attr('data-path');
  }

  /**
   * Update Products List DOM via appending html-list of loaded products
   * to wrapper.
   *
   * @param {string} products - HTML string of fetched product's list
   */
  function updateProductsList(_, products) {
    DOM.$productsList.append(products);
  }

  /**
   * Update loaded products counter by a simple logic:
   * 1) if we have less products left than we can fetch at a time, it means we have loaded them all,
   *    so we should set loaded count a value of total products
   * 2) otherwise, we simply add PRODUCTS_TO_FETCH to counter.
   */
  function updateLoadedCount() {
    DOM.$loadedProducts.text(
      loadedProductsCount() + Math.min(productsLeft(), config.productsToFetch)
    );
  }

  /**
   * Add 'hidden' class to button if there are no more products to load.
   */
  function updateButtonState() {
    if (productsLeft() === 0) {
      DOM.$loadMore.addClass('hidden');
    }
  }

  /**
   * Update view of a product's list.
   *
   * Removes old classes and adds new one depends on what view type was selected.
   * @param {string} viewType: list|tile
   */
  function updateViewType(_, viewType) {
    DOM.$viewType
      .removeClass('view-mode-tile view-mode-list')
      .addClass(`view-mode-${viewType}`);

    if (viewType === DOM.listView.mode) {
      DOM.listView.$.addClass('active');
      DOM.tileView.$.removeClass('active');
    } else {
      DOM.tileView.$.addClass('active');
      DOM.listView.$.removeClass('active');
    }
  }

  /**
   * Return selected sorting option.
   */
  const sortingOption = () => DOM.$sorting.find(':selected');

  /**
   * Number of products remained un-fetched from back-end.
   * Calculates due to a simple formula:
   * left products = total products - already loaded products
   *
   * @returns {Number} - number of products left to fetch
   */
  const productsLeft = () => parseInt(config.totalProductsCount - loadedProductsCount(), 10);

  /**
   * Get number of already loaded products
   *
   * @returns {int} - number of products which are loaded and presented in DOM
   */
  const loadedProductsCount = () => parseInt(DOM.$loadedProducts.first().text(), 10);

  /**
   * Load products from back-end using promise-like fetch object fetchProducts.
   * After products successfully loaded - publishes 'onProductLoad' event.
   */
  function loadProducts() {
    const categoryUrl = DOM.$loadMore.attr('data-url');
    const offset = loadedProductsCount();
    const sorting = sortingOption().val();
    const url = `${categoryUrl}load-more/${offset}/${sorting}`;

    server.fetchProducts(url)
      .then(products => mediator.publish('onProductsLoad', products));
  }

  function buyProduct(event) {
    const buyInfo = () => {
      const product = $(event.target);
      const count = product.closest('.js-order').find('.js-product-count').val();

      return {
        count: parseInt(count, 10),
        id: parseInt(product.attr('productId'), 10),
      };
    };

    const { id, count } = buyInfo();

    server.addToCart(id, count)
      .then(data => mediator.publish('onCartUpdate', data));
  }

  init();
})();
